function openModal(flightId: string) {
	const modal = document.getElementById('flightModal');
	const modalContent = document.getElementById('modal-content');

	// Fetch flight data from Flask API using the flightId (icao24)
	fetch(`/api/get_flight_data/${flightId}`)
		.then((response) => response.json()) // Parse the JSON response
		.then((data) => {
			// Populate the modal with the fetched flight data
			modalContent.innerHTML = `
							<h2>Flight Details</h2>
							<p><strong>Flight Number:</strong> ${data.flight_number}</p>
							<p><strong>Departure:</strong> ${data.departure}</p>
							<p><strong>Arrival:</strong> ${data.arrival}</p>
							<p><strong>Status:</strong> ${data.status}</p>
					`;
			modal.style.display = 'block'; // Show the modal
		})
		.catch((error) => {
			console.error('Error fetching flight data:', error);
			modalContent.innerHTML = '<p>Error loading flight data.</p>';
			modal.style.display = 'block'; // Show modal even in case of error
		});
}
