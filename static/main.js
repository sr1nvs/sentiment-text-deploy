// Emotion mapping dictionary
const emotionMapping = {
    0: "Sadness",
    1: "Joy",
    2: "Love",
    3: "Angry/Neutral",
    4: "Fear",
    5: "Surprise"
};

document.querySelector('form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const text = document.querySelector('#text').value;

    const response = await fetch('/classify', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `text=${encodeURIComponent(text)}`,
    });

    if (response.ok) {
        const data = await response.json();
        console.log(data);
        const resultDiv = document.querySelector('#result');
        if (data && data.Confidence_Values && data.Emotion_Label) {
            resultDiv.innerHTML = `The given text is classified as ${data.Emotion_Label}.<br>`;
            
            // Display each class and its confidence value with corresponding emotion label
            data.Confidence_Values.forEach((confidence, index) => {
                const emotion = emotionMapping[index];
                resultDiv.innerHTML += `${emotion}: ${confidence.toFixed(4)}<br>`;
            });
        } else {
            resultDiv.innerHTML = 'Invalid response data'; // Handle invalid data
        }
    } else {
        console.error('Error classifying text');
    }
});
