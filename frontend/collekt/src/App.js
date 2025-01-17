import React, { useState, useEffect } from 'react';
import './App.css';
import OfferList from './OfferList';
import WishlistForm from './WishlistForm';
import { WebTracerProvider } from '@opentelemetry/sdk-trace-web';
import { FetchInstrumentation } from '@opentelemetry/instrumentation-fetch';
import { BatchSpanProcessor } from '@opentelemetry/sdk-trace-base';
import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-http';


const BACKEND_HOST = "http://localhost/backend";

const provider = new WebTracerProvider();

// Use OTLP HTTP exporter to send traces to Jaeger
const exporter = new OTLPTraceExporter({
  url: 'http://localhost:4317', // Jaeger OTLP endpoint
});

// Use BatchSpanProcessor (recommended for production)
provider.addSpanProcessor(new BatchSpanProcessor(exporter));

provider.register();

function App() {
  const [wishlists, setWishlists] = useState([]);
  const [offers, setOffers] = useState([]);

  // Holen der Wishlist von der API
  useEffect(() => {
    const fetchWishlist = async () => {
      const response = await fetch(`${BACKEND_HOST}/wishlist`);
      const data = await response.json();
      setWishlists(data.items);
    };

    fetchWishlist();
  }, []); // Leeres Array bedeutet, dass der Effekt nur beim ersten Laden ausgeführt wird.

  // Abrufen von Angeboten basierend auf Wishlist-Element
  const fetchOffers = async (wishlistItem) => {
    console.log("Fetching")
    console.log(`${BACKEND_HOST}`)
    
    const response = await fetch(`${BACKEND_HOST}/offerings/${wishlistItem.id}`);
    const data = await response.json();
    setOffers([data]); // Nur ein Angebot wird zurückgegeben, deshalb setzen wir es als Array
  };

   // Wunsch hinzufügen
   const addWish = async (wishlistItem) => {
    console.log("Adding")
    console.log(`${BACKEND_HOST}`)
    const response = await fetch(`${BACKEND_HOST}/wishlist`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(wishlistItem),
    });
    const newItem = await response.json();
    setWishlists([...wishlists, newItem]);
  };

  // Wunsch entfernen
  const removeWish = async (id) => {
    await fetch(`${BACKEND_HOST}/wishlist/${id}`, {
      method: 'DELETE',
    });
    setWishlists(wishlists.filter((wishlist) => wishlist.id !== id));
  };

  return (
    <div className="App">
      <header>
        <h1>Collekt</h1>
        <h1>Produkt Angebote</h1>
      </header>

      <div className="wishlist-section">
        <h2>Produktwünsche</h2>
        <ul>
          {wishlists.map((wishlist) => (
            <li key={wishlist.id}>
              <strong>{wishlist.name}</strong> - <span className="wishlist-description">{wishlist.description}</span>
              <br />
              <br />
              <span className="wishlist-keywords">
                {wishlist.search_terms && wishlist.search_terms.length > 0
                  ? `Suchbegriffe: ${wishlist.search_terms.join(', ')}`
                  : 'Keine Suchbegriffe'}
              </span>
              <br />
              {/* Button zum Laden der Angebote */}
              <button onClick={() => fetchOffers(wishlist)} className="add-btn">
                Angebote anzeigen
              </button>
              {/* Entfernen-Button */}
              <button onClick={() => removeWish(wishlist.id)} className="remove-btn">
                Entfernen
              </button>
            </li>
          ))}
        </ul>
        <WishlistForm addWish={addWish} />
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
