# A simple tip calculator
ratings = ['excellent', 'good', 'poor']
print('A simple tip calculator')
print('Excellent = 25% \nGood = 20% \nPoor = 15%')
service_rating = ''
total_cost = 0
base_cost = float(input('Enter your meal price: '))
''' You don't need this loop; it's just there to make sure the user enters a
valid rating. You could just assume your user is going to play nice or only
allow integer inputs or something. Again, you don't need this loop for this to
to work '''
while service_rating not in ratings:
    print('Please enter Excellent, Good, or Poor')
    service_rating = input('How was the service? ').lower()
if service_rating == 'excellent':
    total_cost = base_cost + (base_cost * 0.25)
if service_rating == 'good':
    total_cost = base_cost + (base_cost * 0.20)
if service_rating == 'poor':
    total_cost = base_cost + (base_cost * 0.15)
print('The total price with tip:\n' + str(round(total_cost, 2)))
