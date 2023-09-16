import cohere
import text_to_speech as tts

# This function takes in 4 dance moves and generates a verse and chorus
def lyrics_generation(prompt1, prompt2, promt3, promt4):
  """
  Generate lyrics based on the given dance moves.

  Parameters:
  - prompt1 (str): The first dance move.
  - prompt2 (str): The second dance move.
  - prompt3 (str): The third dance move.
  - prompt4 (str): The fourth dance move.

  Returns:
    str: The generated lyrics.
  """
  co = cohere.Client('KDT6Iz8B5T3P7KaMDm4dfhusGDtnOAzNGm5YOG38')
  response = co.generate(
    model='command',
    prompt='Your job is to generate the lyrics for a song\'s first verse and the chorus that fits the mood of the varying dance moves prompt. Each dance move will be responsible for a portion of the lyrics. The chorus should have a vibe to match the energy of these dance moves. Put less emphasis on the actual dance move that is prompted, and rather incorporate the themes associated with these various dance moves to create the chorus. Here are the dance move prompts for the first verse:\n\n {}, {}\n\nHere are the dance move prompt for the chorus:\n\n{}, {}'.format(prompt1, prompt2, prompt3, prompt4),
    max_tokens=128,
    temperature=1.5,
    k=0,
    stop_sequences=[],
    return_likelihoods='NONE')
  return('Prediction: {}'.format(response.generations[0].text))


def main():
  lyrics = lyrics_generation('The robot', 'Break Dance', 'Waving hand', 'The moonwalk')
  tts.text_to_speech(lyrics)