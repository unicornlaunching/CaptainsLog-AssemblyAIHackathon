# Here's some code from the inner engine of Captain's Log
# You'll notice the magic happening in prompt=

captains_log_responses = []
promptCount = 0

while promptCount < len(captains_log_prompts):
  # Use chatgpt to generate text
  response = openai.Completion.create(
    engine="text-davinci-003",
    prompt= captains_log_prompts[promptCount] + data_new if promptCount == 0 else captains_log_prompts[promptCount],
    max_tokens=1024,
    n=1,
    temperature=0.5,
  )

  # Print the generated text
  print(response["choices"][0]["text"])
  captains_log_responses.append(response["choices"][0]["text"])
  promptCount+=1
  
  
