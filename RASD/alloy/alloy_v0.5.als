module projectSE2
open util/boolean

abstract sig User{
	device: some SmartDevice,
	email : one Email,
	password : one string,
	name : one string,
	surname: one string
}

sig CarOwner extends User{
	car : set Car,
	schedule : one DailySchedule,
	bookings : set Booking
}

sig ChargingStation{
	owner : one string,
	sockets : disj some Socket,
	availableSockets : one Int,
	occupiedSockets : one Int,
	totalSockets: one Int,
	location : one Location,
}{
	availableSockets>= 0
	totalSockets>= 0
	occupiedSockets >= 0
	}

sig SmartDevice{
	currentLocation : lone Location
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
	status : one Bool,
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
pred show{}

run show{
#CarOwner > 1
#ChargingStation >1
#Socket>2
} for 3
