// Update rating slider values to show the selected number
function updateRatingDisplay() {
	// Navigation rating slider
	document.getElementById('navigationRating').addEventListener('input', function () {
		document.getElementById('navigationValue').textContent = this.value;
	});

	// Speed rating slider
	document.getElementById('speedRating').addEventListener('input', function () {
		document.getElementById('speedValue').textContent = this.value;
	});

	// Accuracy rating slider
	document.getElementById('accuracyRating').addEventListener('input', function () {
		document.getElementById('accuracyValue').textContent = this.value;
	});
}

// Validate form fields
function validateForm() {
	let isValid = true;

	// Validate full name (required)
	const fullName = document.getElementById('fullName').value.trim();
	if (fullName === '') {
		document.getElementById('fullNameError').style.display = 'block';
		isValid = false;
	} else {
		document.getElementById('fullNameError').style.display = 'none';
	}

	// Validate email (required and must be valid format)
	const email = document.getElementById('email').value.trim();
	const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
	if (!emailRegex.test(email)) {
		document.getElementById('emailError').style.display = 'block';
		isValid = false;
	} else {
		document.getElementById('emailError').style.display = 'none';
	}

	// Validate order frequency (required)
	const orderFrequency = document.getElementById('orderFrequency').value;
	if (orderFrequency === '') {
		document.getElementById('orderFrequencyError').style.display = 'block';
		isValid = false;
	} else {
		document.getElementById('orderFrequencyError').style.display = 'none';
	}

	// Validate order device (required)
	const orderDevice = document.querySelector('input[name="orderDevice"]:checked');
	if (!orderDevice) {
		document.getElementById('orderDeviceError').style.display = 'block';
		isValid = false;
	} else {
		document.getElementById('orderDeviceError').style.display = 'none';
	}

	return isValid;
}

// Collect form data
function collectFormData() {
	return {
		fullName: document.getElementById('fullName').value.trim(),
		email: document.getElementById('email').value.trim(),
		phone: document.getElementById('phone').value.trim(),
		orderFrequency: document.getElementById('orderFrequency').value,
		orderDevice: document.querySelector('input[name="orderDevice"]:checked').value,
		navigationRating: document.getElementById('navigationRating').value,
		speedRating: document.getElementById('speedRating').value,
		accuracyRating: document.getElementById('accuracyRating').value,
		features: Array.from(document.querySelectorAll('input[name="features"]:checked')).map(el => el.value),
		improvementSuggestions: document.getElementById('improvementSuggestions').value.trim(),
		timeToOrder: document.getElementById('timeToOrder').value
	};
}

// Handle form submission
function handleFormSubmit(e) {
	e.preventDefault();

	// Validate form
	if (validateForm()) {
		// Collect data
		const formData = collectFormData();

		// Log data to console (for testing)
		console.log('Form data submitted:', formData);

		// Show success message and hide form
		document.getElementById('successMessage').style.display = 'block';
		document.getElementById('feedbackForm').style.display = 'none';

		// In a real application, you would send this data to your server here:
		/*
		fetch('/api/feedback', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify(formData),
		})
		.then(response => response.json())
		.then(data => {
			console.log('Success:', data);
		})
		.catch((error) => {
			console.error('Error:', error);
		});
		*/
	}
}

// Initialize all event listeners when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', function () {
	// Set up rating slider listeners
	updateRatingDisplay();

	// Set up form submission
	document.getElementById('orderFeedback').addEventListener('submit', handleFormSubmit);
});