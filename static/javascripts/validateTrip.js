/**
 * validateTrip.js checks the start and destination of a trip
 */
(() => {

	// Get saved locations from datalist
	const options = document.querySelectorAll('.dl-option');

	// Build hash map of aliases
	const locations = {};

	for (let option of options) {
		locations[option] = true;
	}

	// Validate form
	function validateLocations() {

		// Inputs
		var from = document.querySelector('#from').value;
		var to = document.querySelector('#to').value;

		// Check if input is in datalist
		if (locations[from] && locations[to]) {
			return true;
		} else {
			return false;
		}

	}

})();