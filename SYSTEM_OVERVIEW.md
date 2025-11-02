# AI-Driven Price Drop Alert System

A complete web-based system that tracks product prices in real-time, predicts future price drops using AI, shows historical price data, and allows users to automate purchases via a wallet system.

## Features

### Core Functionality
- **User Authentication**: Secure signup/login using Supabase Auth
- **Product Tracking**: Add products with name, URL, image, and current price
- **Price History**: View 2-month price history with interactive charts
- **AI Price Prediction**: BILSTM-based price prediction (currently using simplified algorithm)
- **Smart Alerts**: Set price drop thresholds with notifications
- **Wallet System**: Manage funds and enable auto-purchase when prices drop
- **Real-time Dashboard**: Beautiful, responsive interface showing all tracked products

### Technical Highlights
- React + TypeScript frontend with Tailwind CSS
- Supabase backend (PostgreSQL database + Edge Functions)
- Chart.js for price visualization
- Row Level Security (RLS) for data protection
- RESTful API architecture

## Architecture

### Frontend (React)
- `src/App.tsx` - Main application component
- `src/contexts/AuthContext.tsx` - Authentication context and state management
- `src/components/Auth.tsx` - Login/signup interface
- `src/components/Dashboard.tsx` - Main dashboard view
- `src/components/ProductCard.tsx` - Product display card
- `src/components/AddProductModal.tsx` - Add new product modal
- `src/components/PriceHistoryModal.tsx` - Price chart visualization
- `src/components/AlertModal.tsx` - Price alert configuration
- `src/components/WalletPanel.tsx` - Wallet management interface
- `src/lib/supabase.ts` - Supabase client configuration

### Backend (Supabase Edge Functions)
- `products` - CRUD operations for products
- `price-history` - Fetch historical price data
- `wallet` - Deposit funds and handle purchases
- `alerts` - Manage price alerts
- `predict` - Generate price predictions

### Database Schema
- `profiles` - User profiles with wallet balance
- `products` - Tracked products with current and predicted prices
- `price_history` - Historical price records
- `alerts` - Price drop alerts with auto-buy settings
- `transactions` - Wallet transaction history

## Getting Started

### Prerequisites
- Node.js 18+
- Supabase account (already configured)

### Environment Variables
The following environment variables are already configured:
- `VITE_SUPABASE_URL` - Supabase project URL
- `VITE_SUPABASE_ANON_KEY` - Supabase anonymous key

### Installation

1. Install dependencies:
```bash
npm install
```

2. Start development server:
```bash
npm run dev
```

3. Build for production:
```bash
npm run build
```

## Usage Guide

### Adding Products
1. Click "Add Product" button on dashboard
2. Enter product name, URL, optional image URL, and current price
3. Product will be added and appear on your dashboard

### Setting Alerts
1. Click "Alert" button on any product card
2. Set your desired price threshold
3. Optionally enable "Auto-Buy" to purchase automatically when threshold is reached
4. Alert will trigger when predicted price drops to or below threshold

### Managing Wallet
1. Click your wallet balance in the navigation bar
2. Enter amount to deposit (simulated transaction)
3. View transaction history
4. Funds will be automatically deducted when auto-buy triggers

### Viewing Price History
1. Click "History" button on any product card
2. View interactive chart showing last 2 months of prices
3. See statistics: current, average, lowest, and highest prices
4. Green dots indicate price drops

### Getting Predictions
1. Click "Predict" button on any product card
2. System will analyze price history and generate prediction
3. Predicted price and trend indicator will appear on the card
4. Alerts will automatically check if threshold is met

## AI Price Prediction

### Current Implementation
The system currently uses a simplified prediction algorithm that:
- Analyzes recent price trends
- Calculates average price
- Applies trend extrapolation
- Adds controlled volatility simulation

### Advanced Implementation (BILSTM)
A full BILSTM model implementation is provided in `bilstm_model.py`:
- Bidirectional LSTM architecture
- 60-day sequence length
- 3-layer deep network with dropout
- Trained on historical price data
- Can be deployed as a separate Python microservice

To upgrade to BILSTM:
1. Install Python dependencies: `pip install tensorflow numpy pandas scikit-learn`
2. Collect sufficient historical price data (100+ days per product)
3. Train the model using `bilstm_model.py`
4. Deploy as REST API (Flask example included)
5. Update the `predict` Edge Function to call your Python API

## API Endpoints

All Edge Functions are available at:
`https://[your-project].supabase.co/functions/v1/[function-name]`

### Products API
- `GET /products` - List all user's products
- `POST /products` - Add new product
- `DELETE /products/:id` - Delete product

### Price History API
- `GET /price-history?product_id=xxx` - Get product price history

### Wallet API
- `POST /wallet/deposit` - Add funds to wallet
- `POST /wallet/purchase` - Process purchase
- `GET /wallet/transactions` - Get transaction history

### Alerts API
- `GET /alerts?product_id=xxx` - Get product alerts
- `POST /alerts` - Create new alert
- `PUT /alerts` - Update alert
- `DELETE /alerts?alert_id=xxx` - Delete alert

### Prediction API
- `POST /predict` - Generate price prediction

## Security

- JWT-based authentication
- Row Level Security (RLS) on all tables
- Users can only access their own data
- Secure password hashing
- Protected API endpoints
- Input validation

## Future Enhancements

1. **Real Price Scraping**: Integrate web scraping to automatically fetch current prices
2. **Email Notifications**: Send alerts via email when prices drop
3. **Mobile App**: React Native version for iOS/Android
4. **Social Features**: Share deals with friends
5. **Price Comparison**: Compare prices across multiple retailers
6. **Advanced Analytics**: More detailed price trend analysis
7. **Scheduled Updates**: Automatic daily price checks
8. **Export Data**: Download price history as CSV
9. **Browser Extension**: Track prices while browsing
10. **Real Payment Integration**: Connect Stripe for actual purchases

## Development

### Running Tests
```bash
npm test
```

### Type Checking
```bash
npm run typecheck
```

### Linting
```bash
npm run lint
```

### Building
```bash
npm run build
```

## Tech Stack

- **Frontend**: React 18, TypeScript, Tailwind CSS, Chart.js
- **Backend**: Supabase (PostgreSQL, Edge Functions)
- **Authentication**: Supabase Auth
- **Deployment**: Vite build system
- **AI/ML**: TensorFlow/Keras (BILSTM model)

## License

This project is provided as-is for educational and development purposes.
