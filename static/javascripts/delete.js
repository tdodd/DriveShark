(() => {

	const deleteIcons = document.querySelectorAll('.delete-icon');

	// Add listeners to delete icons
	for (const icon of deleteIcons) {
		icon.addEventListener('click', event => confirmDelete(event));
	}

	/**
	 * Prompt a user to confirm deletion of an element
	 *
	 * @param {DOMEvent} event the event that is being confirmed
	 * @return {void}
	 */
	function confirmDelete(event) {

		if(!confirm('Are you sure?')) {
			event.preventDefault();
		}

	}

})();