//Gather all a tags that store discussion prompt questions on the given page and store them in an array
let discussionPromptArray = document.querySelectorAll('.od-section ul li a[href*="discussionPrompt"]');

//intialize an object to store their IDs
let idObject = {};

//Parse the stringified objects, then gather the itemId property from each, finally storing it in the idObject and marking it as completed
discussionPromptArray.forEach(item =>
    idObject[(JSON.parse(item["dataset"]["clickValue"])["itemId"])] = "Completed"
);

//Then, store the completed itemIds in the localCourseProgress object in localStorage
localStorage.setItem('localCourseProgress~85718863~8D3R5HiaEeioIg7r4jw_PA', JSON.stringify(idObject));

//Get previously stored items from localStorage so that we can add new items on the coming pages without overwriting previous items
let stored = JSON.parse(localStorage.getItem('localCourseProgress~85718863~8D3R5HiaEeioIg7r4jw_PA'));

//From here, we can repeat steps 1, 2, 3 and 5 on the new page and then add them to the stored object, then add that stored object back to localStorage
for(const property in idObject){
    stored[`${property}`] = `${idObject[property]}`
}

//Then set the stored object that we've just modified as the new item we add to local storage
localStorage.setItem('localCourseProgress~85718863~8D3R5HiaEeioIg7r4jw_PA', JSON.stringify(stored));