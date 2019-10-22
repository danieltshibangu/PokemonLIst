from flask import Flask, render_template, url_for, request, redirect, current_app, flash
# get access to the form 
from pkmnForm import pokemonSubmit

# this uses the flask constructor to connect flask to the main output 
app = Flask( __name__ )

#configure a secret key for csrf protection
# config loads the current configuration change to an object that 
# affects all other extentions, files, etc 
app.config[ "SECRET KEY"] = "WGNy;2An6=}_&Fod1Tq~D!4_lu3/7[c?H!xcJG[Lr77wQX66]4XJigy_;n6K"
app.app_context() 

# create a list that stores pokemon; includes sample pokemon already 
pokemonList = [ "Pikachu", "Bulbasaur", "Squirtle", "Charmander" ]

# create a route for the site 
@app.route( '/pokeList', methods=[ 'POST', 'GET' ])
def pokeList(): 
	# create a form variable that initializes the class 
	form = pokemonSubmit()
	# this validate function returns True if form is submitted 
	# using a POST request AND it is valid 
	if form.validate_on_submit():
		# from the form, the name variable inside the function, and data gets it 
		pokemonName = form.name.data

		if pokemonName not in pokemonList: 
			pokemonList.append( pokemonName )
			flash( "Pokemon added!", 'success' )
		else: 
			flash( "Pokemon already added!", 'failure' ) 
		
		print( "\nData Recieved...Now redirecting.")
		return redirect( request.url )

	return render_template( "pkmnHTML.html", form=form )

if __name__ == "__main__":
	app.run( debug=True )
