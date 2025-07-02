import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import App from '../App';

test('renders the main heading', () => {
  render(<App />);
  // Adjusted to match actual heading text in App.jsx
  const headingElement = screen.getByText(/Job Dashboard/i);
  expect(headingElement).toBeInTheDocument();
});
