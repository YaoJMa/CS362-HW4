def cube_vol(vol):
	return vol

l = float(input("Enter a length to find volume of cube: "))
vol = l * l * l
	
if type(vol) not in [int, float]:
		raise TypeError("Length needs to be a valid integer or float")
	
print("Volume of cube: ", vol) 
