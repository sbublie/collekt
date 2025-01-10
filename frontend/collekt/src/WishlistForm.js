import React, { useState } from 'react';

function WishlistForm({ addWishlist }) {
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');
  const [keywords, setKeywords] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    const wishlist = {
      name,
      description,
      keywords: keywords.split(',').map((keyword) => keyword.trim()),
    };
    addWishlist(wishlist);
    setName('');
    setDescription('');
    setKeywords('');
  };

  return (
    <div className="wishlist-form">
      <h2>Wishlist hinzufügen</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Name der Wishlist"
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
        <button type="submit">Wishlist hinzufügen</button>
      </form>
    </div>
  );
}

export default WishlistForm;
