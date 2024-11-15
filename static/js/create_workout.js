function selectWeek(week) {
    const selectedWeeks = document.getElementsByClassName('selected_week');
    for (let i = 0; i < selectedWeeks.length; i++) {
        selectedWeeks[i].value = week;
    }

    console.log(week);
}

function selectDay(day) {
    const selectedDays = document.getElementsByClassName('selected_day');
    for (let i = 0; i < selectedDays.length; i++) {
        selectedDays[i].value = day;
    }
}

function addNewWeek(week) {
    // Define the HTML structure for the new week
    const newWeekHTML = `
        <div class="col-12 text-center mt-3 mb-3">
            <h2 class="logo-font text-black">Week ${week}</h2>
            <textarea class="form-control pseudo-p" id="weekly-desc${week}" name="weekly-desc${week}" rows="4" placeholder="Enter description for the week *Optional*"></textarea>
        </div>
        <div class="row g-3 justify-content-center w-100" id="days-container-${week}">
        </div>
        <div class="col-12">
            <div class="text-center mt-3">
                <button 
                    onclick="addNewWeek(${week + 1})" 
                    class="btn btn-black" id ="add-week-button">
                    Add Week
                </button>
            </div>
        </div>`;

    // Append the new week section to the "weeks-and-days" container
    const container = document.getElementById(`weeks-and-days`);
    if (document.getElementById("add-week-button")){
        document.getElementById("add-week-button").remove()
    }
    container.insertAdjacentHTML("beforeend", newWeekHTML);
    selectWeek(week)
    if(week>1){
        addNewDay(week,1)
    }
    
    // Save the current week count to localStorage
    localStorage.setItem("lastWeek", week);
}

function addNewDay(week, day) {
    // Define the new day card HTML without the "Add Day" button if day is 7
    let newDayHTML = `
        <div class="col-sm-12 col-md-6 col-lg-4 col-xl-2 mt-3 ml-3">
            <div class="card h-100 text-black card-shadow" style="width: 18rem;">
                <div class="card-body" id="${week}-${day}" onclick="selectDay(${day}); selectWeek(${week});">
                    <h5 class="card-title text-center">Day: ${day}</h5>
                </div>
            </div>
        </div>`;

    // Only add "Add Day" button if day is less than 7
    if (day < 7) {
        newDayHTML += `
            <div class="col-sm-12 col-md-6 col-lg-4 col-xl-2 mt-3 ml-3 add-day-button-${week}">
                <div class="card h-100 text-black card-shadow" style="width: 18rem;">
                    <div class="card-body">
                        <h5 class="card-title text-center">Add new day</h5>
                        <div class="text-center mt-3">
                            <button 
                                onclick="addNewDay(${week}, ${day + 1})" 
                                class="btn btn-black">
                                Add Day
                            </button>
                        </div>
                    </div>
                </div>
            </div>`;
    }

    // Get the container for the specified week
    const container = document.getElementById(`days-container-${week}`);
    const addDayButtons = document.querySelectorAll(`.add-day-button-${week}`);

    // If there are add-day-buttons, remove the last one before adding the new content
    if (addDayButtons.length > 0) {
        addDayButtons[addDayButtons.length - 1].remove();
    }

    // Insert the new HTML at the end of the container
    container.insertAdjacentHTML("beforeend", newDayHTML);

    // Set the selected day and store the last day in localStorage
    selectDay(day);
    localStorage.setItem(`lastDay-week-${week}`, day);
}


function resetWeeks() {
    localStorage.removeItem("lastWeek");
    document.getElementById("weeks-and-days").innerHTML = ""; // Clears the container
    addNewWeek(1); // Optionally, add the first week again
    localStorage.removeItem("new_workout");
    localStorage.clear()
    const resetWorkoutUrl = "/workouts/reset_workout/";

    console.log("Resetting weeks...");

    // Use fetch API to make a POST request to a Django view
    fetch(resetWorkoutUrl, {  // The URL of your Django view
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value // Django CSRF token for security
        },
        body: JSON.stringify({
            // Any data you want to send to the server
            message: "Reset workout data"
        })
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response data from the server
        if (data.success) {
            alert("Workout has been reset!");
        } else {
            alert("Error resetting workout.");
        }
    })
    .catch(error => {
        console.error("Error:", error);
    });
    location.reload();
}
 // Load saved weeks from localStorage on page load
 document.addEventListener("DOMContentLoaded", () => {
    // Get the last saved week and last saved day from localStorage
    const lastWeek = localStorage.getItem("lastWeek");
    const startingWeek = lastWeek ? parseInt(lastWeek) : 1;

    // Generate all saved weeks up to the last saved week count
    for (let week = 1; week <= startingWeek; week++) {
        addNewWeek(week);

        // For each week, get the last saved day and determine the starting day
        const lastDay = localStorage.getItem(`lastDay-week-${week}`);
        const startingDay = lastDay ? parseInt(lastDay) : 1;

        // Generate all days up to the last saved day for this week
        for (let day = 1; day <= startingDay; day++) {
            addNewDay(week, day);
        }
    }

    // Retrieve the workout data from localStorage
    const storedWorkout = JSON.parse(localStorage.getItem("new_workout"));
    console.log(storedWorkout);

    // If there are stored exercises, recreate the <p> tags for each
    if (storedWorkout) {
        for (const key in storedWorkout) {
            const exercise = storedWorkout[key];
            const { exercise_name, sets, reps, week, day } = exercise;

            // Create a new <p> tag if exercise_name exists
            if (exercise_name) {
                const pTag = document.createElement("p");
                pTag.className = "card-text text-center";
                pTag.textContent = `${exercise_name}   S:${sets} R:${reps}`;

                // Find the target div for the week and day and append the <p> tag
                const targetDiv = document.getElementById(`${week}-${day}`);
                if (targetDiv) {
                    targetDiv.appendChild(pTag); // Append the <p> tag to the target div
                } else {
                    console.warn(`Target div with id "${week}-${day}" not found.`);
                }
            }
        }
    }
    attachExerciseFormListeners()
});



// Add event listener to each form's button to handle submission
function attachExerciseFormListeners() {
    document.querySelectorAll(".exercise-form button").forEach(button => {
        button.addEventListener("click", function(event) {
            event.preventDefault(); // Prevent form submission

            const form = event.target.closest('form'); // Get the closest form element
            const exerciseId = form.querySelector("input[name='exercise_id']").value;
            const sets = form.querySelector("input[name='sets']").value;
            const reps = form.querySelector("input[name='reps']").value;
            const day = form.querySelector("input.selected_day").value;
            const week = form.querySelector("input.selected_week").value;
            const redirectUrl = form.querySelector("input[name='redirect_url']").value;
            const exerciseName = form.querySelector("input[name='exercise_name']").value; // Get exercise name

            // Validate sets input
            if (!sets) {
                alert("You didn't enter any sets");
                return; // Stop the function if validation fails
            }

            // Generate a unique ID for this exercise entry
            const randomId = crypto.randomUUID();

            // Retrieve existing workout data from localStorage or initialize new
            const newWorkout = JSON.parse(localStorage.getItem("new_workout")) || {};

            // Add new exercise to the workout data
            newWorkout[randomId] = {
                exercise_id: exerciseId,
                exercise_name: exerciseName,
                sets: sets,
                reps: reps,
                day: day,
                week: week
            };

            // Create the new <p> element for the exercise details
            const pTag = document.createElement("p");
            pTag.className = "card-text text-center";
            pTag.textContent = `${exerciseName} S:${sets} R:${reps}`;

            // Find the target div based on the week and day
            const targetDiv = document.getElementById(`${week}-${day}`);
            if (targetDiv) {
                targetDiv.appendChild(pTag); // Append the <p> tag to the target div
            } else {
                console.warn(`Target div with id "${week}-${day}" not found.`);
            }

            // Save the updated workout data to localStorage
            localStorage.setItem("new_workout", JSON.stringify(newWorkout));

            // Optionally, redirect to the specified URL after adding the exercise
            fetch("/workouts/update_workout_session/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": form.querySelector("[name='csrfmiddlewaretoken']").value // Include CSRF token
                },
                body: JSON.stringify({
                    new_workout: newWorkout
                })
            })
            .then(response => response.json())
            .then(data => {
                // Handle server response if necessary
                console.log("Data successfully saved to session:", data);
            })
            .catch(error => {
                console.error("Error sending data to server:", error);
            });
            
        });
    });
}

function searchExercises() {
    const searchQuery = document.getElementById("search-exercises").value;
    const searchExercisesUrl = "/workouts/search_exercises/"; 
    
    fetch(searchExercisesUrl, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value, // CSRF token
        },
        body: JSON.stringify({ query: searchQuery }), // Send query in the request body
    })
    .then(response => response.json())
    .then(data => {
        const exercisesContainer = document.getElementById("all-exercises");
        exercisesContainer.innerHTML = ""; // Clear previous results

        if (data.success) {
            // Populate exercises dynamically
            data.exercises.forEach(exercise => {
                // Create the outermost div with classes
                const outerDiv = document.createElement("div");
                outerDiv.className = "col-sm-12 col-md-6 col-lg-3 col-xl-3 mt-3";
            
                // Create the card div
                const cardDiv = document.createElement("div");
                cardDiv.className = "card";
            
                // Create the card body div
                const cardBodyDiv = document.createElement("div");
                cardBodyDiv.className = "card-body";
            
                // Create the title
                const title = document.createElement("h5");
                title.className = "card-title";
                title.textContent = exercise.name;
            
                // Create the description
                const description = document.createElement("p");
                description.className = "card-text";
                description.textContent = exercise.description;
            
                // Create the form
                const form = document.createElement("form");
                form.className = "d-inline exercise-form";
                form.setAttribute("data-exercise-id", exercise.id);
            
                // Add CSRF token (this will not work without being server-rendered; you may need to append it dynamically if necessary)
                const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
                form.innerHTML = `
                    <input type="hidden" name="csrfmiddlewaretoken" value="${csrfToken}">
                    <input type="hidden" name="exercise_id" value="${exercise.id}">
                    <input type="hidden" name="exercise_name" value="${exercise.name}">
                    <input type="hidden" name="redirect_url" value="${window.location.pathname}">
                    <input type="number" name="sets" id="sets">
                    <label for="sets">Sets</label>
                    <input type="number" name="reps" id="reps">
                    <label for="reps">Reps</label>
                    <input type="hidden" class="selected_day" name="day" value="1">
                    <input type="hidden" class="selected_week" name="week" value="1">
                    <button type="button" class="btn btn-black">Add</button>
                `;
            
                // Append title, description, and form to the card body
                cardBodyDiv.appendChild(title);
                cardBodyDiv.appendChild(description);
                cardBodyDiv.appendChild(form);
            
                // Append card body to card div
                cardDiv.appendChild(cardBodyDiv);
            
                // Append card to outermost div
                outerDiv.appendChild(cardDiv);
            
                // Append outermost div to the container
                exercisesContainer.appendChild(outerDiv);
                attachExerciseFormListeners()
            });
            
        } else {
            alert("Error: " + data.error);
        }
    })
    .catch(error => {
        console.error("Error:", error);
    });
}

