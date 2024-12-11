import json

# Correct file path
file_path = '/workspace/Workout-Tracker/exercises/fixtures/exercises.json'

# Open and read the file
with open(file_path, 'r') as file:
    data = json.load(file)

# Update the image_url fields
for entry in data:
    if "fields" in entry and "image_url" in entry["fields"]:
        old_url = entry["fields"]["image_url"]
        
        # Extract the image filename (without path and extension)
        path_parts = old_url.split('/')  # Split the URL by '/' to get parts
        filename = path_parts[-1]  # Get the filename (last part of the URL)
        name, extension = filename.split('.')  # Split filename and extension
        
        # Capitalize the first letter of each word in the filename and replace underscores with hyphens
        capitalized_name = '-'.join([word.capitalize() for word in name.split('-')])  # Capitalize each word
        
        # Construct the new URL with the capitalized name and .webp extension
        new_url = f"/static/media/exercises/{capitalized_name}.{extension}"
        
        # Update the image_url field
        entry["fields"]["image_url"] = new_url

# Save the updated data back to the file or a new file
output_path = '/workspace/Workout-Tracker/exercises/fixtures/updated_exercises.json'
with open(output_path, 'w') as file:
    json.dump(data, file, indent=4)


