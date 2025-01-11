import React, { useState } from 'react';

function WishlistForm({ addWish }) {
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');
  const [keywords, setKeywords] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const wishlistItem = {
      id: Date.now().toString(),  // Eine einfache ID mit dem aktuellen Timestamp
      name,
      description,
      search_terms: keywords.split(',').map((keyword) => keyword.trim()),
    };
    addWish(wishlistItem);
    setName('');
    setDescription('');
    setKeywords('');
  };

  return (
    <div className="wishlist-form">
      <h2>Produktwunsch hinzufügen</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Name des Produktes"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Beschreibung"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Suchbegriffe (durch Komma getrennt)"
          value={keywords}
          onChange={(e) => setKeywords(e.target.value)}
          required
        />
        <button type="submit">Produktwunsch hinzufügen</button>
      </form>
    </div>
  );
}

export default WishlistForm;
