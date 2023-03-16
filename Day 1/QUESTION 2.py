## Booking a flight ticket in which a adult price cost 37550 and including service task 7% and
## due to festival season 10 % off on final ticket
n = int(input("no of Adult"))
c = int(input("no of child"))
Adult = n*37550.0
child = c*37550.0/3
service = 7/100*(Adult+child)
total = Adult+child+service
discount = 10/100*total

print(total-discount)
