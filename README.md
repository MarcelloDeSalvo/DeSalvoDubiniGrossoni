# Nuxt 3 Minimal Starter

Look at the [Nuxt 3 documentation](https://nuxt.com/docs/getting-started/introduction) to learn more.

[de-salvo-dubini-grossoni.vercel.app](https://de-salvo-dubini-grossoni.vercel.app)

## Local Setup

Make sure to install the dependencies:

```bash
# 1] install Node
install Node https://nodejs.org/it/

# 2] clone the repo
git clone https://github.com/MarcelloDeSalvo/SE2nuxtjs.git

# 3] make a .env file in the root directory and write
BACKEND_URL=your_backend_url
ex: BACKEND_URL=http://127.0.0.1:8000

# 4] install Yarn while inside the root folder
npm install --global yarn

# 5] install all dependencies
yarn

# 6] Start the development server
yarn run dev
```

## Error fix
- about_Execution_Policies: https://bobbyhadz.com/blog/yarn-cannot-be-loaded-running-scripts-disabled]

## Development Server

Start the development server on http://localhost:3000

```bash
yarn run dev
```

## Production

Build the application for production:

```bash
yarn run build
```

Check out the [deployment documentation](https://nuxt.com/docs/getting-started/deployment) for more information.
