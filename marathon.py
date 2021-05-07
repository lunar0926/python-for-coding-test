def solution(participant, completion):
    participant_dict = {name : 0 for name in participant}
    for name in participant:
        participant_dict[name] += 1
    
    completion_dict = {name : 0 for name in participant}
    for name in completion:
        completion_dict[name] += 1
        
    for name in participant:
        if participant_dict[name] != completion_dict[name]:
            return name
