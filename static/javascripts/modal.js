/**
 * Show and hide the location modal
 */
(() => {

	const locationBtn = document.querySelector('.add-location');
	const locationModal = document.querySelector('#location-modal');
	const overlay = document.querySelector('.overlay');

	// The duration of the modal animation (in ms)
	const hideAnimationDuration = 300;

	// Add listeners for modal show/hide
	locationBtn.addEventListener('click', event => showModal());
	overlay.addEventListener('click', event => {
		if (!overlay.classList.contains('hidden')) { hideModal(); }
	});

	/**
	 * Show the location modal and the overlay
	 *
	 * @return void
	 */
	function showModal() {
		overlay.style.height = getDocumentHeight();
		overlay.classList.remove('hidden');
		locationModal.classList.add('modal-in');
		locationModal.classList.remove('hidden');
	}

	/**
	 * Hide the location modal and the overlay
	 *
	 * @return void
	 */
	function hideModal() {
		overlay.classList.add('hidden');
		locationModal.classList.remove('modal-in');
		locationModal.classList.add('modal-out');
		setTimeout(() => {
			locationModal.classList.add('hidden');
			locationModal.classList.remove('modal-out');
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