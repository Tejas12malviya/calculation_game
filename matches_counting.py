teams=int(input('Enter the number of teams:'))
qualifiers_matches=int(input('Enter the number of quilifiers:'))
round=int(input('Enter the number of rounds in tournament:'))
group=int(input('Enter the number of groups in tournament:'))

team_in_each_group=teams/group
match_by_each_team=(team_in_each_group-1)*round
matches=(match_by_each_team*team_in_each_group)*group

total_matches=qualifiers_matches+matches
print('Total matches in the tournament:',total_matches)