## Description:
	Given a balance on a gift card, this program will find the sum of 2 or 3 items that are equivalent, or closest to, 
	the gift card balance.


## Dependencies:
	Python 3.x 


## Instructions to Run:
	python3 giftCard.py <file> <number> <balance>
		-file: .txt file containing a list of sorted items
		-number: Number of gifts to select
		-balance: Balance of the gift card


## Examples:
	$ python3 giftCard.py prices.txt 2 2300
	Paperback Book 700, Headphones 1400

	$ python3 giftCard.py prices.txt 2 1100
	Not possible

	$ python3 giftCard.py prices.txt 3 7700
	Paperback Book 700, Detergent 1000, Bluetooth Stereo 6000
	

## Notes:
	twoGifts: O(n)
	threeGifts: O(n^2)
