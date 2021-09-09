let discussionPromptArray = document.querySelectorAll('.od-section ul li a[href*="discussionPrompt"]');

let objectArray = [];

discussionPromptArray.forEach(item => objectArray.push(item['dataset']['clickValue']));

objectArray.forEach(object => object['isNextItemInCourse'] = false);