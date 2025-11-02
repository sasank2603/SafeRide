# Quick Start Guide

## What You Have

A fully functional AI-driven price drop alert system with:

✅ User authentication (signup/login)
✅ Product tracking with price monitoring
✅ AI-powered price prediction
✅ Interactive price history charts (2 months)
✅ Smart alerts with customizable thresholds
✅ Digital wallet for auto-purchase
✅ Beautiful, responsive UI
✅ Secure database with Row Level Security
✅ RESTful API via Supabase Edge Functions

## Getting Started

### 1. Start the Application

The development server starts automatically. Your app is running at the provided URL.

### 2. Create Your Account

1. Open the application in your browser
2. Click "Sign Up"
3. Enter your name, email, and password
4. You'll be automatically logged in

### 3. Add Your First Product

1. Click the "Add Product" button
2. Fill in the product details:
   - **Name**: e.g., "Wireless Headphones"
   - **URL**: The product page URL
   - **Image URL** (optional): Direct link to product image
   - **Current Price**: e.g., 99.99
3. Click "Add Product"

### 4. Set Up Price Alerts

1. Find your product card on the dashboard
2. Click the "Alert" button
3. Set your target price (e.g., $79.99)
4. Optionally enable "Auto-Buy" for automatic purchase
5. Click "Create Alert"

### 5. Add Funds to Wallet

1. Click your wallet balance in the top navigation
2. Enter an amount (e.g., 500)
3. Click "Deposit"
4. Your balance will update immediately

### 6. Generate Price Predictions

1. Click the "Predict" button on any product card
2. The system analyzes price history and generates a prediction
3. View the predicted price and trend indicator
4. If your alert threshold is met, it will automatically trigger

### 7. View Price History

1. Click the "History" button on any product
2. See an interactive chart of the last 2 months
3. View statistics: current, average, min, and max prices
4. Green dots show price drops

## Key Features Explained

### Price Prediction Algorithm

Currently uses a simplified prediction model that:
- Analyzes recent price trends
- Calculates moving averages
- Applies trend extrapolation
- Simulates market volatility

**Upgrade to BILSTM**: See `bilstm_model.py` for a full deep learning implementation

### Auto-Buy Feature

When enabled:
1. System checks predicted price against your threshold
2. If price ≤ threshold and wallet has sufficient funds
3. Purchase is automatically executed
4. Transaction is recorded in your wallet history
5. Balance is updated

### Security

- All user data is protected with Row Level Security
- Users can only access their own products, alerts, and transactions
- Passwords are securely hashed
- JWT-based authentication

## API Endpoints

All Edge Functions are accessible at:
`https://[your-project].supabase.co/functions/v1/[function-name]`

### Available Functions:
- `products` - Manage products
- `price-history` - Get price data
- `wallet` - Manage funds
- `alerts` - Set up alerts
- `predict` - Generate predictions

## Example Workflow

1. **Sign Up** → Create account with email/password
2. **Add Product** → "Sony WH-1000XM5" at $399.99
3. **Set Alert** → Notify me when price ≤ $299.99
4. **Add Funds** → Deposit $500 to wallet
5. **Enable Auto-Buy** → Purchase automatically at target price
6. **Run Prediction** → System predicts next price
7. **View History** → See 2-month price trend
8. **Get Notified** → Alert triggers when threshold met
9. **Auto-Purchase** → System buys product if auto-buy enabled

## Tips

- Add multiple products to track different items
- Set realistic alert thresholds based on price history
- Keep sufficient wallet balance for auto-purchases
- Run predictions regularly to catch price drops
- Check transaction history to monitor purchases

## Next Steps

### Enhance with Real Data:
1. Integrate web scraping for automatic price updates
2. Connect to e-commerce APIs (Amazon, eBay, etc.)
3. Schedule daily price checks
4. Send email notifications

### Upgrade AI Model:
1. Install Python dependencies: `pip install tensorflow numpy pandas scikit-learn`
2. Collect 100+ days of historical data per product
3. Train BILSTM model using `bilstm_model.py`
4. Deploy as Python microservice
5. Update predict Edge Function to call your API

### Add Features:
- Email notifications
- Mobile app version
- Social sharing
- Price comparison across retailers
- Export data to CSV
- Browser extension for tracking

## Troubleshooting

**Can't sign in?**
- Check email and password
- Ensure you've created an account first

**Product not appearing?**
- Refresh the page
- Check browser console for errors

**Prediction not working?**
- Ensure product has price history
- Try again in a few seconds

**Auto-buy not triggering?**
- Check wallet balance
- Verify alert threshold is set correctly
- Ensure auto-buy is enabled

## Support

For technical details, see `SYSTEM_OVERVIEW.md`
For BILSTM implementation, see `bilstm_model.py`

## Database Schema

- **profiles**: User info + wallet balance
- **products**: Tracked products with prices
- **price_history**: Historical price records
- **alerts**: Price drop alerts
- **transactions**: Wallet activity

All tables have Row Level Security enabled.

---

**You're all set!** Start tracking prices and let the AI help you find the best deals.
