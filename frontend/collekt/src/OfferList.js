import React from 'react';

function OfferList({ offers }) {
  if (offers.length === 0) {
    return <p>Keine Angebote gefunden.</p>;
  }

  return (
    <div className="offer-list">
      {offers.map((offer) => (
        <div key={offer.id} className="offer-item">
          <h3>{offer.title}</h3>
          <p><strong>Preis:</strong> {offer.price}</p>
          <p><strong>Shop:</strong> {offer.store}</p>
          <a href={offer.link} target="_blank" rel="noopener noreferrer">Mehr erfahren</a>
        </div>
      ))}
    </div>
  );
}

export default OfferList;
