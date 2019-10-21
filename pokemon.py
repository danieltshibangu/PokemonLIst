from flask import Flask, render_template, url_for, request
# this uses the flask constructor to connect flask to the main output 
app = Flask( __name__ )

#configure a secret key for csrf protection
# config loads the current configuration change to an object that 
# affects all other extentions, files, etc 
app.config[ "SECRET KEY"] = "WGNy;2An6=}_&Fod1Tq~D!4_lu3/7[c?H!xcJG[Lr77wQX66]4XJigy_;n6K"
app.app_context() 

# create a list that stores pokemon 
pokemonList = [ "Pikachu", "Bulbasaur", "Squirtle", "Charmander" ]

# create a route for the site 
app.route( 'pokeList', methods=[ 'POST', 'GET' ])
def pokeList(): 
	message = ""
	if request.method = 'POST': 
		pokemonName = request.form.get( "pokemon_Name" )
		pokemonList.append( pokemonName )
		message = "Pokemon added!"

		if pokemonName in pokemonList:
			message = "Pokemon already added!"

	return render_template( "pkmnHTML.html", message=message )

if __name__ == "__main__":
	app.run( debug=True )
