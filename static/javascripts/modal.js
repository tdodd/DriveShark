/**
 * Show and hide modals
 */
(() => {

	// Modal triggers
	const triggers = document.querySelectorAll('.trigger');

	// Black page overlay
	const overlay = document.querySelector('.overlay');

	// The duration of the modal animation (in ms)
	const hideAnimationDuration = 300;

	// Add listeners for modal show/hide
	for (const trigger of triggers) {
		trigger.addEventListener('click', event => showModal(event.target));
	}

	// Hide modal on overlay click
	overlay.addEventListener('click', event => {

		if (!overlay.classList.contains('hidden')) {
			hideModal();
		}

	});

	/**
	 * Show the location modal and the overlay
	 *
	 * @param {Node} trigger the trigger that was clicked
	 * @return void
	 */
	function showModal(trigger) {
		console.log('cliked')


		// If button is not disabled
		if (!trigger.parentElement.hasAttribute('disabled')) {

			// Show overlay
			overlay.style.height = getDocumentHeight();
			overlay.classList.remove('hidden');

			// Show modal
			const modal = document.querySelector('#' + trigger.dataset.triggerid);
			modal.classList.remove('hidden');
			modal.classList.add('modal-in');
			modal.classList.add('modal-showing');

		}

	}

	/**
	 * Hide the location modal and the overlay
	 *
	 * @return void
	 */
	function hideModal() {
		overlay.classList.add('hidden');
		const modal = document.querySelector('.modal-showing');
		modal.classList.remove('modal-in');
		modal.classList.add('modal-out');
		setTimeout(() => {
			modal.classList.add('hidden');
			modal.classList.remove('modal-out');
			modal.classList.remove('modal-showing');
		}, hideAnimationDuration);
	}

	/**
	 * Get the full height of the html document
	 *
	 * @return {string} the height of the document in pixels
	 */
	function getDocumentHeight() {
		const body = document.body;
		const html = document.documentElement;
		return Math.max(body.scrollHeight, body.offsetHeight, html.clientHeight, html.scrollHeight, html.offsetHeight) + 'px';
	}

})();