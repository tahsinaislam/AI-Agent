
class MonsterClassificationAgent:
    def __init__(self):
        #If you want to do any initial processing, add it here.
        pass

    def solve(self, samples, new_monster):

        all_sizes = []
        all_colors = []
        all_coverings = []
        all_foot_types =[]
        all_leg_counts =[]
        all_arms = [] 
        all_eyes = []
        all_horns = [] 


        for monster in samples:
            if monster[1] == True:
                all_sizes.append(monster[0]['size'])
                all_colors.append(monster[0]['color'])
                all_coverings.append(monster[0]['covering'])

        
        
        if new_monster['size'] in all_sizes:
            if new_monster['covering'] in all_coverings:
                if new_monster['color'] in all_colors:
                    return True
                else:
                    return False
            else: 
                return False
        else:
            return False
    

      
        #Add your code here!
        #
        #The first parameter to this method will be a labeled list of samples in the form of
        #a list of 2-tuples. The first item in each 2-tuple will be a dictionary representing
        #the parameters of a particular monster. The second item in each 2-tuple will be a
        #boolean indicating whether this is an example of this species or not.
        #
        #The second parameter will be a dictionary representing a newly observed monster.
        #
        #Your function should return True or False as a guess as to whether or not this new
        #monster is an instance of the same species as that represented by the list.
        pass