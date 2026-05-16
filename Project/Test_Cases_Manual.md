Test ID	Function	Input	Expected Output
TC01	add_student	"Ali"	"Ali added."
TC02	add_student (duplicate)	"Ali"	"Ali already exists."
TC03	add_grade	"Ali", 85	"Grade 85 added for Ali."
TC04	add_grade (invalid)	"Ali", 105	"Invalid grade."
TC05	calculate_average	"Ali"	85.0
TC06	pass_fail	"Ali"	"Pass"
TC07	pass_fail (no grades)	"Sara"	"No grades for Sara."