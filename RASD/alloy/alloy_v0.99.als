module projectSE2
open util/boolean

abstract sig User{
	device : disj one SmartDevice,
	email : one Email,
	password : one string,
	name : one string,
	surname : one string
}

one sig System{
	cpms : some CPMS,
	users : some User
}

sig CarOwner extends User{
	car : set Car,
	schedule : one DailySchedule,
	suggestedChargingTimes : set Event,
	suggestedChargingLocations : set Location,
	bookings : set Booking,
	nextTrip : lone Route,
	nearStations : set ChargingStation
}

sig CPOoperator extends User{
	company : one CPO
}

sig ChargingStation{
	owner : one CPO,
	sockets : disj some Socket,
	totalSockets : one Int,
	location : one Location,
	currentEnergySource : one EnergySource,
	battery : disj one Battery		
}{
	totalSockets = #sockets
	totalSockets>0
}

sig Socket{
	chargingSpeed : one Int,
	occupied : one Bool,
	bookings : Booking,
	socketType : one string,
	connectedCar : lone Car
}

sig CPO{}

sig CPMS{
	CPOowner : one CPO,
	operators : set CPOoperator,
	chargingStations : disj some ChargingStation,
	allOffers : disj set Offer,
	connectedDSO : some DSO,
	offers : allOffers-> some chargingStations
}{
	#operators>0
}

abstract sig EnergySource{}

sig Battery extends EnergySource{}

sig DSO extends EnergySource{
	price : one Eprice
}

sig Eprice{}

sig Offer{
	author : one CPOoperator,
	value : one Value,
	startingDate : one Date,
	endingDate : one Date,
}{
	startingDate != endingDate
}

sig Value{
	tens : one Int,
	units : one Int
}{
	tens>=0
	units >=0
	tens + units > 0 //offer cannot be 0% discount 
}
 
sig SmartDevice{
	currentLocation : one Location
}

sig Location{
	coordinates : one Coordinates
}

sig Coordinates{
	longitude : one Int,
	latitude : one Int
}

sig Route{
	stops : some Location
}

sig Email{}
sig string{}

sig Car{
	batteryPercent : one Int, 
	maker : one string
}

sig Booking{
	location : one Location,
	time : one Date,
	socket : one Socket,
	user : one Email
}

sig DailySchedule{
	events : set Event
}

sig Event{
	location : one Location,
	time : one Date
}

sig Date{}


// -------FACTS --------

//different charging stations cannot share a socket
fact socketHasOneChargingStation{
	all s : Socket | no disj cs1, cs2 : ChargingStation | s in cs1.sockets and s in cs2.sockets
}

//CPO operators are registered only in CPMSs owned by their company
fact correctOperators{
	all cpow : CPOoperator, cpms : CPMS | cpow in cpms.operators iff cpow.company = cpms.CPOowner
}

//there are no sockets without charging stations
fact socketIsInCS{
	all s : Socket | one cs : ChargingStation | s in cs.sockets
}

//a chaging station must be nearby the user if it is in the user's near stations
fact nearbyStationsConditions{
	all cs : ChargingStation, u : CarOwner | cs in u.nearStations iff cs.location=u.device.currentLocation
}

//all charging stations are owned by a CPO
fact noWildChargingStation{
	all cs : ChargingStation | one cpms: CPMS | cs in cpms.chargingStations
}

//no uregistered users or CPMSs
fact allUsersRegistered{
	all u : User | one s : System | u in s.users}

fact allCPMSInSystem{
	all ms : CPMS | one s : System | ms in s.cpms}

//each charging station in a cpms must share the owner with the cpms itself
fact sameOwner{
all cpms : CPMS | all cs : ChargingStation | cs in cpms.chargingStations iff cs.owner=cpms.CPOowner
}

//no car has 2 different owners
fact noCarHasTwoOwners{
	all c : Car | no disj u1, u2 : CarOwner | c in u1.car and c in u2.car
}

//all cars have a registered user
fact allCarsHaveOwners{
	all c : Car | one u : CarOwner | c in u.car
}

fact chargingSocketsHaveCarsConnected{
	all c : Car, s:Socket |all u : CarOwner, cs : ChargingStation | 
		(c in s.connectedCar) implies
		(s.occupied.isTrue and u.device.currentLocation=cs.location  and s in cs.sockets and c in u.car)
}

//all users have unique emails
fact DifferentMails{
	no disj u1, u2 : User | u1.email=u2.email
}

//each registered operator must work for a CPO
fact allOperatorsWorkForCompanies{
	all o : CPOoperator, cpms : CPMS | o.company = cpms.CPOowner implies o in cpms.operators
}

//all bookings belongs to users
fact trueBookings{
	all b : Booking | all u : User | b.user=u.email iff b in u.bookings
}

//no different sockets have same booking
fact {
	no disj s,s1 : Socket | some b : Booking | b in s.bookings and b in s1.bookings
}

//the relation booking to socket must be reflected in the relation socket to booking
fact BookingToSocketRelation{
	no b : Booking, s : Socket | b in s.bookings and b.socket != s
}

//mapping email and users
fact noWildEmails{
	all e : Email | one u : User | e = u.email
}

//no shared schedules
fact DifferentSchedules{
	no disj c1,c2 : CarOwner| c1.schedule = c2.schedule
}

//no shared devices
fact noSameDevice{
	no disj  c1,c2 : CarOwner| c1.device = c2.device
}

// all charging station locations are distinct
fact noSameLocationForCS{
	no disj cs1, cs2 : ChargingStation | cs1.location = cs2.location
}

//when the reservation is stored, location in the reservation should match the location of the charging station booked
fact BookingRightLocation{
	all b : Booking, cs : ChargingStation | b in  cs.sockets.bookings iff b.location=cs.location
}

//no disjointed locations have the same coordinates
fact allLocationsAreDifferent{
	no disj l1,l2 : Location | l1.coordinates=l2.coordinates and 
		l1.coordinates.latitude=l2.coordinates.latitude and
		l1.coordinates.longitude=l2.coordinates.longitude
}

//for an offer to be valid, the author must work for the company where the offer is applied
fact allOffersAreLegitimate{
	all cpms : CPMS, offer : Offer | offer in cpms.allOffers iff offer.author in cpms.operators
}

//an user cannot be in two different places at once
fact noOverlappingEventsForUser{
	all ds : DailySchedule | no disj e1, e2 : Event | e1 in ds.events and e2 in ds.events and e1.time = e2.time
}

//for a time suggestion, the event must take place near a charging station
fact SuggestCorrectly{
	all c : CarOwner, e : Event | one cs : ChargingStation | e.location=cs.location 
		and e in c.schedule.events 
			and e in c.suggestedChargingTimes
}

//for a route suggestion, the charging station must be along the predicted route
fact SuggestLocationsCorrectly{
	all c : CarOwner, place : Location | one cs : ChargingStation | 
	place in c.suggestedChargingLocations iff (place in c.nextTrip.stops and place = cs.location)
}

//all schedules belong to users
fact noWildSchedules{
	all s : DailySchedule | one sys : System | s in sys.users.schedule
}

//all devices belong to users
fact noWildDevices{
	all d : SmartDevice | one sys : System | d in sys.users.device
}

//all registered location have a point of interest
fact noWildLocations{
	all l : Location | one sys : System | 
		l in sys.users.device.currentLocation 
		or l in sys.users.schedule.events.location 
		or l in sys.cpms.chargingStations.location
}

//all bookings are registered in the charging station
fact allBookingsAreRegistered{
	all b : Booking | one cs : ChargingStation| b.location=cs.location and b in cs.sockets.bookings
}

fact noWildValues{
	all v : Value | one sys : System | v in sys.cpms.allOffers.value
}

fact allCPOinSystem{
	all cpo : CPO | one sys : System | cpo in sys.cpms.CPOowner
}

fact chargingStationsDoNotStealEnergy{
	all cs : ChargingStation, cpms:CPMS | cs in cpms.chargingStations implies (cs.currentEnergySource in cpms.connectedDSO or cs.currentEnergySource=cs.battery)
}

fact noWildDSO{
	all dso : DSO | one sys : System | dso in sys.cpms.connectedDSO
}

fact noWildBattery{
	all b : Battery | one sys : System | b in sys.cpms.chargingStations.battery
}

fact noWildRoute{
	all r:Route | one sys : System | r in sys.users.nextTrip
}

fact noWildEprice{
	all eprice : Eprice | one sys: System | eprice in sys.cpms.connectedDSO.price
}

//given a user and a charging station, details of the charging station are returned only if the user is nearby
fun ChargingStationIsNearby[co:CarOwner, cs:ChargingStation]: lone ChargingStation{
	{return : ChargingStation | (return=cs iff co.device.location=cs.location)
	}
}

// --------- ASSERTIONS & PREDICATES ---------


//G1. Know about the charging stations nearby
assert CorrectNearby{
 all disj co:CarOwner, cs:ChargingStation | 
 cs in ChargingStationIsNearby[co, cs] iff co.device.location=cs.location
}

pred NearbyStation[u:CarOwner]{
	#u.nearStations>0
}





//G2. Book a charge in a specific charging station for a certain timeframe
assert BookingsAreRegistered{
	all b: Booking, cs : ChargingStation, c : CarOwner, sys:System | 
			(b in c.bookings iff 
						b.user=c.email and c in sys.users) 
			and (b in cs.sockets.bookings  iff 
						b.location = cs.location 
						and b.socket in cs.sockets )
}

pred bookingRequest[b:Booking, co:CarOwner, cs:ChargingStation]{
	(b in co.bookings) implies
		(b.user=co.email) 
	and (b in cs.sockets.bookings) implies
		(b.location = cs.location 
		and b.socket in cs.sockets)
}

//G3. & G12. Start the Charging process at a specific station
pred ChargingProcess[co: CarOwner, cs: ChargingStation, s: Socket, b:Booking, c:Car]{
	co.device.currentLocation = cs.location 
	and s in cs.sockets 
	and s.occupied.isTrue 
	and b in co.bookings 
	and b in s.bookings
	and c in co.car
	and c in s.connectedCar
}

//G5. Be able to communicate with multiple CPMS
pred multipleCPMS[cpms1 : CPMS, cpms2 : CPMS, sys : System]{
	cpms1 in sys.cpms
	and cpms2 in sys.cpms
	and cpms1 != cpms2
}

//G6. Suggest the user convenient charging timeframes based on his upcoming schedule.
assert SuggestionWorksCorrectly{
	all c: CarOwner, e: Event | some cs:ChargingStation | 
		e in c.suggestedChargingTimes iff 
		e.location in cs.location 
		and e in c.schedule.events 
}

//G6. Suggest the user convenient charging timeframes based on his next trip.
assert LocationSuggestionWorksCorrectly{
	all c:CarOwner, place:Location | some cs: ChargingStation|
	place in c.suggestedChargingLocations iff
	(
		place in c.nextTrip.stops and cs.location=place
	)
}

//G9. Be able to communicate with at least one DSO
assert CommunicateWithSomeDSO{
	all CPms : CPMS | some dso : DSO | one sys : System | 
	CPms in sys.cpms implies 
	dso in CPms.connectedDSO
}

//G15. cpms - Dynamically decide where to get energy for charging (station battery or DSO)
//G16. cpow - change the source of energy between batteries and grid
pred switchSource[b : Battery, dso : DSO, cs1 : ChargingStation, cs2 : ChargingStation]{
	cs1 != cs2 
	and cs1.currentEnergySource=b
	and cs1.battery=b
	and cs2.currentEnergySource=dso
}

//G17. Insert special and limited offers
assert OfferValidity{
	all offer:Offer, cpms:CPMS, cs:ChargingStation, sys:System |
	(offer->cs) in cpms.offers implies 
		(offer.author in sys.users 
		and offer.author.company=cpms.CPOowner 
		and cpms.CPOowner = cs.owner and offer in cpms.allOffers 
		and cs in cpms.chargingStations)
}

pred show{}

check OfferValidity for 10
check CorrectNearby for 10
check SuggestionWorksCorrectly for 10
check LocationSuggestionWorksCorrectly for 10
check BookingsAreRegistered for 10 
check CommunicateWithSomeDSO for 10


run switchSource for 10
run NearbyStation for 10
run ChargingProcess for 10
run bookingRequest for 10
run multipleCPMS for 10

run show{
	#CPMS >1
	#Location > 4
	#User<5
	#Car <4
	#Offer<3
	#DSO>1
} for 15

run show{
} for 10
