from flask import Flask, render_template, url_for, request
# this uses the flask constructor to connect flask to the main output 
app = Flask( __name__ )

# make a list of popular cartoons 
Pokemons =["Pikachu", "Charizard", "Squirtle", "Jigglypuff",
			"Bulbasaur", "Gengar", "Charmander", "Mew", "Lugia", "Gyarados"]

# the route will connect to home at extension '/' or '/home'
@app.route( '/' )
# this definition contains the contents of the home page
def home(): 
	# this uses the html format from the html file as substitute
	return render_template( 'practice_home.html', pokemon=Pokemons, length=len(Pokemons))
'''
@app.route( '/home', methods=[ 'POST', 'GET' ])
def result():
	if request.method == 'POST':
		result = request.form
		render_template( 'practice_home.html', result=result )
'''

# call the main function under a conditional to avoid errors
# run the program if the debugger comes back as true 
if __name__ == "__main__":
	app.run( debug=True )
