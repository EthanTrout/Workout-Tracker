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

function addNewDay(week,day){
    if(day<=6){
        newDayHTML = `<div class="col-sm-12 col-md-6 col-lg-4 col-xl-2 mt-3 ml-3">
                    <div class="card h-100 text-black card-shadow" style="width: 18rem;">
                        <div class="card-body" id=${week}-${day}>
                            <h5 class="card-title text-center">Day:${day}</h5>
                        </div>
                    </div>
                </div>
                <div class="col-sm-12 col-md-6 col-lg-4 col-xl-2 mt-3 ml-3" id="add-day-button">
                    <div class="card h-100 text-black card-shadow" style="width: 18rem;">
                        <div class="card-body">
                            <h5 class="card-title text-center">Add new day</h5>
                            <div class="text-center mt-3">
                                <button 
                                    onclick="addNewDay(${week},${day+1})" 
                                    class="btn btn-black">
                                    Add Day
                                </button>
                            </div>
                        </div>
                    </div>
                </div>`

        const container = document.getElementById(`days-container-${week}`);
        if (document.getElementById("add-day-button")){
            document.getElementById("add-day-button").remove()
        }
        container.insertAdjacentHTML("beforeend", newDayHTML);
        selectDay(day)
        localStorage.setItem(`lastDay-week-${week}`, day);
    }
    else{
        newDayHTML = `<div class="col-sm-12 col-md-6 col-lg-4 col-xl-2 mt-3 ml-3">
                    <div class="card h-100 text-black card-shadow" style="width: 18rem;">
                        <div class="card-body" id=${week}-${day}>
                            <h5 class="card-title text-center">Day:${day}</h5>
                        </div>
                    </div>
                </div>`

        const container = document.getElementById(`days-container-${week}`);
        if (document.getElementById("add-day-button")){
            document.getElementById("add-day-button").remove()
        }
        container.insertAdjacentHTML("beforeend", newDayHTML);
        selectDay(day)
        localStorage.setItem(`lastDay-week-${week}`, day);
    }
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
    const urlParams = new URLSearchParams(window.location.search);
            if (urlParams.has('created') && urlParams.get('created') === 'true') {
                console.log("Form successfully submitted!");
                resetWeeks()
                window.location.replace('/workouts')
            }
        
});



// Add event listener to each form's button to handle submission
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