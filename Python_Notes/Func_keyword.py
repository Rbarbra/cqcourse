def greeting(Name,msg="Good Morning!"):
	print("Hello", Name + ', ' + msg)

greeting(Name = "Christoph",msg = "How do you do?")
greeting(msg = "How do you do?",Name = "Christoph") 
greeting("Christoph", msg = "How do you do?")