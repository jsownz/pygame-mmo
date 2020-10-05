import character

def earn_xp(amount):
  character_data = character.get_character()

  currentXP = int(character_data["characterXP"])
  newXP = currentXP + amount
  print(f'CurrentXP: {str(currentXP)}, amount: {str(amount)}, newXP: {str(newXP)}')
  character.store_info([{'characterXP': newXP}])
