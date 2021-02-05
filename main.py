# please import vehicle_class.py module here

### We are developing a program for a car delaership to
# inventory for used cars. The delearship inventory includes 
## three types of automobiles: cars, pick up and SUVs.
## The class information is in vehicles class module.

import vehicles_class as vc #vehicles.py
def vehicle_info(vehicle_list):
	print('USED CARS INVENTORY')
	print('The following vehicles are in inventory:')
	print('========================================')
	count = 1
	for vehicle in vehicle_list:
		print('(',count,')')  
		print(vehicle)
		if vehicle == car:
			print('Number of doors are: ', vehicle.get_doors())
		elif vehicle == truck:
			print('The drive type is: ', truck.get_drive_type())
		else:
				print('The passenger capacity is: ', vehicle.get_pass_cap())
		print('************************************')
		count += 1
# call the function
car = vc.Car('Mercedes-Benz', 'CLS', 2013, 74850, 35000.0, 4)
truck = vc.Truck('Toyota', 'Tundra', 2012, 40000, 32000.0, '4WD')
suv = vc.SUV('BMW', 'X5', 2015, 55600, 48500.0, 5)
vehicle_info([car, truck, suv])

'''

#car_truck_SUV_instances.py
import vehicles_class as vc #vehicles.py
# create intances
my_car = vc.Car('Mercedes-Benz', 'CLS', 2013, 74850, 35000.0, 4)
print(my_car)
print('The car has',my_car.get_doors(), 'doors')
# create SUV instance (object)
my_SUV = vc.SUV('Honda', 'Pilot', 2015, 78000, 25000, '5')
print(my_SUV)
print('The SUV is', my_SUV.get_pass_cap(),'passengers type' )
# crreate instance for pick up truck 
'''
