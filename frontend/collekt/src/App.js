import React, { useState } from 'react';
import './App.css';
import OfferList from './OfferList';
import WishlistForm from './WishlistForm';

function App() {
  const [wishlists, setWishlists] = useState([]);
  const [offers, setOffers] = useState([]);
  const [selectedWishlist, setSelectedWishlist] = useState(null);

  // Mock für die Angebote basierend auf einer Wishlist
  const fetchOffers = (wishlist) => {
    // Hier wird nur eine Simulation von Angeboten verwendet, basierend auf den Suchbegriffen der Wishlist.
    const fakeOffers = [
      { id: 1, title: 'Produkt 1', price: '29,99 €', store: 'Store A', link: '#' },
      { id: 2, title: 'Produkt 2', price: '49,99 €', store: 'Store B', link: '#' },
      { id: 3, title: 'Produkt 3', price: '19,99 €', store: 'Store C', link: '#' },
    ];
    setOffers(fakeOffers); // Simulierte API-Daten setzen
  };

  // Wunschliste hinzufügen
  const addWishlist = (wishlist) => {
    setWishlists([...wishlists, wishlist]);
  };

  // Funktion zum Entfernen einer Wishlist
const removeWishlist = (id) => {
  setWishlists(wishlists.filter((wishlist) => wishlist.id !== id));
};

  return (
    <div className="App">
      <header>
        <h1>Collekt</h1>
        <h1>Produkt Angebote</h1>
      </header>

      <div className="wishlist-section">
        <h2>Wishlists</h2>
        <ul>
          {wishlists.map((wishlist, index) => (
            <li key={index}>
              <strong>{wishlist.name}</strong> - <span className="wishlist-description">{wishlist.description}</span>
              <br />
              <br />
              <span className="wishlist-keywords">
                {wishlist.keywords && wishlist.keywords.length > 0
                  ? `Suchbegriffe: ${wishlist.keywords.join(', ')}`
                  : 'Keine Suchbegriffe'}
              </span>
              <br />
              {/* Button zum Laden der Angebote */}
              <button onClick={() => fetchOffers(wishlist)} className='add-btn'>
                Angebote anzeigen
              </button>
              {/* Entfernen-Button */}
              <button onClick={() => removeWishlist(wishlist.id)} className="remove-btn">
                Entfernen
              </button>
            </li>
          ))}
        </ul>
        <WishlistForm addWishlist={addWishlist} />
      </div>

      {/* Anzeige der Angebote */}
      {offers.length > 0 && (
        <div className="offer-list">
          <h2>Angebote</h2>
          <OfferList offers={offers} />
        </div>
      )}
    </div>
  );
}

export default App;
