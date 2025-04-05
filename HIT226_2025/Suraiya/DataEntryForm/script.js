/**
 * LearningPath - Study Session Tracker
 * Main JavaScript functionality for form handling and validation
 */

document.addEventListener('DOMContentLoaded', function () {
	// DOM elements
	const studyForm = document.getElementById('study-form');
	const successMessage = document.getElementById('success-message');
	const productivitySlider = document.getElementById('productivity');
	const productivityValue = document.getElementById('productivity-value');
	const objectivesContainer = document.getElementById('objectives-container');
	const addObjectiveBtn = document.getElementById('add-objective');

	// Set default date to today
	initializeDate();

	// Event listeners
	productivitySlider.addEventListener('input', updateProductivityValue);
	addObjectiveBtn.addEventListener('click', addNewObjective);
	initializeRemoveButtonListeners();
	studyForm.addEventListener('submit', handleFormSubmit);

	/**
	 * Set the date input to today's date
	 */
	function initializeDate() {
		const today = new Date().toISOString().split('T')[0];
		document.getElementById('date').value = today;
	}

	/**
	 * Update the productivity rating display
	 */
	function updateProductivityValue() {
		productivityValue.textContent = this.value;
	}

	/**
	 * Add a new learning objective field
	 */
	function addNewObjective() {
		const newObjective = document.createElement('div');
		newObjective.className = 'objective-item';
		newObjective.innerHTML = `
            <input type="text" name="objectives[]" placeholder="e.g., Understood concept X" required>
            <button type="button" class="remove-objective" title="Remove objective">✕</button>
        `;
		objectivesContainer.appendChild(newObjective);

		// Add event listener to the new remove button
		const removeBtn = newObjective.querySelector('.remove-objective');
		removeBtn.addEventListener('click', handleRemoveObjective);
	}

	/**
	 * Initialize listeners for the initial remove button
	 */
	function initializeRemoveButtonListeners() {
		const removeButtons = document.querySelectorAll('.remove-objective');
		removeButtons.forEach(button => {
			button.addEventListener('click', handleRemoveObjective);
		});
	}

	/**
	 * Handle removing an objective
	 */
	function handleRemoveObjective() {
		if (objectivesContainer.children.length > 1) {
			this.parentElement.remove();
		} else {
			alert('You need at least one learning objective');
		}
	}

	/**
	 * Handle form submission and validation
	 */
	function handleFormSubmit(e) {
		e.preventDefault();

		// Reset previous errors
		hideAllErrors();

		// Validate form
		if (validateForm()) {
			submitForm();
		}
	}

	/**
	 * Hide all error messages
	 */
	function hideAllErrors() {
		document.querySelectorAll('.error').forEach(el => {
			el.style.display = 'none';
		});
	}

	/**
	 * Validate all form fields
	 * @returns {boolean} Whether the form is valid
	 */
	function validateForm() {
		let isValid = true;

		// Validate subject
		const subject = document.getElementById('subject').value.trim();
		if (!subject) {
			document.getElementById('subject-error').style.display = 'block';
			isValid = false;
		}

		// Validate topic
		const topic = document.getElementById('topic').value.trim();
		if (!topic) {
			document.getElementById('topic-error').style.display = 'block';
			isValid = false;
		}

		// Validate date
		const date = document.getElementById('date').value;
		if (!date) {
			document.getElementById('date-error').style.display = 'block';
			isValid = false;
		}

		// Validate duration
		const duration = document.getElementById('duration').value;
		if (!duration || duration < 5 || duration > 480) {
			document.getElementById('duration-error').style.display = 'block';
			isValid = false;
		}

		// Validate objectives
		const objectives = document.querySelectorAll('input[name="objectives[]"]');
		let hasValidObjective = false;
		objectives.forEach(obj => {
			if (obj.value.trim()) hasValidObjective = true;
		});

		if (!hasValidObjective) {
			document.getElementById('objectives-error').style.display = 'block';
			isValid = false;
		}

		return isValid;
	}

	/**
	 * Submit the form data
	 */
	function submitForm() {
		// Collect form data
		const formData = collectFormData();

		// Log for demonstration (would be sent to server in real app)
		console.log('Form submitted successfully!');
		console.log('Form Data:', formData);

		// Show success message
		studyForm.style.display = 'none';
		successMessage.style.display = 'block';

		// Reset form after a delay
		setTimeout(resetForm, 3000);
	}

	/**
	 * Collect all form data into an object
	 * @returns {Object} Form data object
	 */
	function collectFormData() {
		const objectives = Array.from(
			document.querySelectorAll('input[name="objectives[]"]')
		).map(obj => obj.value.trim()).filter(Boolean);

		return {
			subject: document.getElementById('subject').value.trim(),
			topic: document.getElementById('topic').value.trim(),
			date: document.getElementById('date').value,
			duration: document.getElementById('duration').value,
			productivity: document.getElementById('productivity').value,
			environment: document.getElementById('environment').value,
			notes: document.getElementById('notes').value,
			objectives: objectives
		};
	}

	/**
	 * Reset the form to its initial state
	 */
	function resetForm() {
		studyForm.reset();
		initializeDate();
		productivityValue.textContent = '7';

		// Reset objectives to just one
		objectivesContainer.innerHTML = `
            <div class="objective-item">
                <input type="text" name="objectives[]" placeholder="e.g., Understood concept X" required>
                <button type="button" class="remove-objective" title="Remove objective">✕</button>
            </div>
        `;

		// Re-add event listener to the remove button
		initializeRemoveButtonListeners();

		// Show form again, hide success message
		studyForm.style.display = 'block';
		successMessage.style.display = 'none';
	}
});