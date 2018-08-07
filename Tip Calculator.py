# A simple tip calculator
ratings = ['excellent', 'good', 'poor']
print('A simple tip calculator')
print('Excellent = 25% \nGood = 20% \nPoor = 15%')
serviceRating = ''
totalCost = 0
baseCost = float(input('Enter your meal price: '))
while serviceRating not in ratings:
    print('Please enter Excellent, Good, or Poor')
    serviceRating = input('How was the service? ').lower()
if serviceRating == 'excellent':
    totalCost = baseCost + (baseCost * 0.25)
if serviceRating == 'good':
    totalCost = baseCost + (baseCost * 0.20)
if serviceRating == 'poor':
    totalCost = baseCost + (baseCost * 0.15)
print('The total price with tip:\n' + str(round(totalCost, 2)))
