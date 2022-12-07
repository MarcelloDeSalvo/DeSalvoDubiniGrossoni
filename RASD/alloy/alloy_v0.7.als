module projectSE2
open util/boolean

abstract sig User{
	device: one SmartDevice,
	email : one Email,
	password : one string,
	name : one string,
	surname: one string
}

sig CarOwner extends User{
	car : set Car,
	schedule : one DailySchedule,
	suggestedChargingTimes: set Event,
	bookings : set Booking
}

sig ChargingStation{
	owner : one string,
	sockets : disj some Socket,
	totalSockets: one Int,
	location : one Location,
}{
	totalSockets = #sockets
	totalSockets>0
	}
 
sig SmartDevice{
	currentLocation : one Location
}

sig CPOoperator extends User{
	company : one string
}

sig Location{
	coordinates : one Coordinates
}

sig Coordinates{
	longitude : one Int,
	latitude : one Int
}

sig Email{}
sig string{}

sig Socket{
	chargingSpeed : one Int,
	occupied: one Bool,
	bookings : Booking,
	socketType : one string
}

sig Car{
	batteryPercent: one Int, 
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

sig CPMS{
	CPOowner : one string,
	chargingStations : disj some ChargingStation,
}

one sig System{
	cpms : some CPMS,
	users : some User
}

//a socket is only in one charging station
fact socketHasOneChargingStation{
	all s: Socket | no disj cs1, cs2 : ChargingStation | s in cs1.sockets and s in cs2.sockets
}

//there are no sockets without charging stations
fact socketIsInCS{
	all s: Socket | one cs : ChargingStation | s in cs.sockets
}

//all charging stations are owned by a CPO
fact noWildChargingStation{
	all cs : ChargingStation | one cpms: CPMS | cs in cpms.chargingStations
}

//no uregistered users or CPMSs
fact allUsersRegistered{
	all u: User | one s: System | u in s.users}

fact allCPMSInSystem{
	all ms:CPMS | one s:System | ms in s.cpms}

//charging stations in cpms and the cpms itself have the same CPO owner
fact sameOwner{
all cpms: CPMS | all cs : ChargingStation | cs in cpms.chargingStations iff cs.owner=cpms.CPOowner
}

//no car has 2 different owners
fact noCarHasTwoOwners{
	all c : Car | no disj u1, u2 : CarOwner | c in u1.car and c in u2.car
}

//all cars have a registered user
fact allCarsHaveOwners{
	all c: Car | one u: CarOwner | c in u.car
}

fact DifferentMails{
	no disj u1, u2: User | u1.email=u2.email
}

//all bookings belongs to users
fact {
	all b: Booking | all u : User | b.user=u.email iff b in u.bookings
}

//no different sockets have same booking
fact {
	no disj s,s1:Socket | some b:Booking | b in s.bookings and b in s1.bookings
}

//mapping booking and sockets
fact BookingToSocketRelation{
	no b: Booking, s: Socket | b in s.bookings and b.socket != s
}

//mapping email and users
fact noWildEmails{
	all e: Email | one u: User | e = u.email
}

//no shared schedules
fact DifferentSchedules{
	no disj c1,c2: CarOwner| c1.schedule = c2.schedule
}

//no shared devices
fact noSameDevice{
	no disj  c1,c2: CarOwner| c1.device = c2.device
}

// all charging station locations are distinct
fact noSameLocationForCS{
	no disj cs1, cs2: ChargingStation | cs1.location = cs2.location
}

//when the reservation is stored, location in the reservation should match the location of the charging station booked
fact BookingRightLocation{
	all b: Booking, cs:ChargingStation | b in  cs.sockets.bookings iff b.location=cs.location
}

//no disjointed locations have the same coordinates
fact allLocationsAreDifferent{
	no disj l1,l2 : Location | l1.coordinates=l2.coordinates and 
		l1.coordinates.latitude=l2.coordinates.latitude and
		l1.coordinates.longitude=l2.coordinates.longitude
}

fact noOverlappingEventsForUser{
	all ds: DailySchedule | no disj e1, e2: Event | e1 in ds.events and e2 in ds.events and e1.time = e2.time
}

fact SuggestCorrectly{
	all c: CarOwner, e: Event | one cs :ChargingStation | e.location=cs.location 
		and e in c.schedule.events 
			and e in c.suggestedChargingTimes
}

fact noWildSchedules{
	all s:DailySchedule | one sys:System | s in sys.users.schedule
}

fact noWildDevices{
	all d:SmartDevice | one sys:System | d in sys.users.device
}

fact noWildLocations{
	all l:Location | one sys:System | l in sys.users.device.currentLocation or l in sys.users.schedule.events.location or l in sys.cpms.chargingStations.location
}

fact allBookingsAreRegistered{
	all b:Booking | one cs:ChargingStation| b.location=cs.location and b in cs.sockets.bookings
}




//verify that all the bookings made are registered to the right user, and location and socket of the charging station matches correctly
assert BookingsAreRegistered{
	all b: Booking, cs : ChargingStation, c : CarOwner | 
			(b in c.bookings iff 
						b.user=c.email) 
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

//verify that only correct suggestions are made
assert SuggestionWorksCorrectly{
	all c: CarOwner, e: Event | some cs:ChargingStation | 
		e in c.suggestedChargingTimes iff 
		e.location in cs.location 
		and e in c.schedule.events
}

fun ChargingStationIsNearby[co:CarOwner, cs:ChargingStation]: lone ChargingStation{
	{return: ChargingStation | (return=cs iff co.device.location=cs.location)
	}
}

assert CorrectNearby{
 all disj co:CarOwner, cs:ChargingStation | cs in ChargingStationIsNearby[co, cs] iff co.device.location=cs.location
}

pred ChargingProcess[co: CarOwner, cs: ChargingStation, s: Socket, b:Booking]{
	co.device.currentLocation = cs.location and s in cs.sockets and s.occupied.isTrue and b in co.bookings and b in s.bookings
}

check CorrectNearby for 10

check SuggestionWorksCorrectly for 10

check BookingsAreRegistered for 10 

pred show{}

run ChargingProcess for 10
run bookingRequest
run show{
#CarOwner > 1
#ChargingStation >1
#Socket>2
#Event>2
} for 4
