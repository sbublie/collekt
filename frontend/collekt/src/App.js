import React, { useState } from 'react';
import './App.css';
import OfferList from './OfferList';

function App() {
  const [searchQuery, setSearchQuery] = useState('');
  const [offers, setOffers] = useState([]);

  const handleSearch = async () => {
    // Hier würdest du eine echte API-Anfrage machen, die Angebote zurückgibt.
    // Für dieses Beispiel simulieren wir eine API-Antwort.
    const fakeOffers = [
      { id: 1, title: 'Produkt 1', price: '29,99 €', store: 'Store A', link: '#' },
      { id: 2, title: 'Produkt 2', price: '49,99 €', store: 'Store B', link: '#' },
      { id: 3, title: 'Produkt 3', price: '19,99 €', store: 'Store C', link: '#' },
    ];

    setOffers(fakeOffers); // Simulierte API-Daten setzen
  };

  return (
    <div className="App">
      <header>
        <h1>Collekt - Produkt Angebote</h1>
        <div className="search-bar">
          <input
            type="text"
            placeholder="Nach Produkten suchen..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
          />
          <button onClick={handleSearch}>Suchen</button>
        </div>
      </header>

      <OfferList offers={offers} />
    </div>
  );
}

export default App;
