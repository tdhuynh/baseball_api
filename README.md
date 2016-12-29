# baseball_api

# Objective
* Create an API of CRUD views for Django models.

# Features:
* List all models for a given resource localhost:8000/api/:resource_name/
* Retrieve a specific instance for a given resource (by pk) localhost:8000/api/:resource_name/:pk/
* Create a Master model through a POST request to the localhost:8000/api/:resource_name/ url
* Create a Batting and Pitching, and Fielding model through a POST request that tie back to a Master record.
* Update existing fields on an existing Master, Batting, Pitching and Fielding resources.
* Delete an existing Master, Batting, Pitching, and Fielding model.
