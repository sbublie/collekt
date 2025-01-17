import React from 'react';

function OfferList({ offers }) {
  if (offers.length === 0) {
    return <p>Keine Angebote gefunden.</p>;
  }
  console.log(offers);

  return (
    <div className="offer-list">
      {offers[0].map((offer) => (
        <div key={offer.wishlist_item_id} className="offer-item">
          {/* Angebotstitel, hier nehme ich an, dass du ihn im Backend hinzufügst */}
          <h3>Produktangebot</h3>
          <p><strong>Titel:</strong> {offer.title} </p>
          <p><strong>Preis:</strong> {offer.price} €</p>
          <p><strong>Link:</strong> <a href={offer.url} target="_blank" rel="noopener noreferrer">Mehr erfahren</a></p>
        </div>
      ))}
    </div>
  );
}

export default OfferList;
