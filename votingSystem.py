#candidates
candidate1 = input('Enter the name of 1st nominee: ')
candidate2 = input('Enter the name of 2do nominee: ')

cd1_votes = 0
cd2_votes = 0

voter_id = [1,2,3,4,5,6,7,8,9,10]

quantityVoter = len(voter_id)

while True:
    if voter_id == []:  # to check when voter list is complted
        print('Voting session is over!!')
        if cd1_votes > cd2_votes:
            percent = (cd1_votes/quantityVoter)*100
            print(candidate1, 'has won the election with', percent, '% of votes')
            break
        elif cd2_votes > cd1_votes:
            percent = (cd2_votes/quantityVoter)*100
            print(candidate2, 'has won the election with', percent, '% of votes')
            break 
        else:
            print('Both have number of votes!! Goverment will  decide who will rule')
            break

    voter = int(input('Enter your voter id: '))
    if voter in voter_id:
        print("You're a voter")
        voter_id.remove(voter) # it'll remove for no voting again
        print('_______________________')
        print(f'To give vote to {candidate1} press 1')
        print(f'To give vote to {candidate2} press 2')
        print('___________________________')
        vote = int(input('Enter your vote: '))
        if vote == 1:
            cd1_votes +=1
            print(candidate1, 'Thank you for your vote!!')
        elif vote == 2:
            cd2_votes +=1
            print(candidate2, 'Thank you for your vote!!')    
        elif vote > 2:
            print('Check your pressed key !!')    

        else:
            print('You are not a voter or you have voted already')    