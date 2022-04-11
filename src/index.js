const express = require('express')
const morgan = require('morgan')
const exphbs = require('express-handlebars')
const path = require('path')
const flash = require('connect-flash')
const session = require('express-session')
const MySqlStore = require('express-mysql-session')
const passport = require('passport')
const { database } = require('./keys')
const { isLoggedIn, error404 } = require('./lib/auth')
// const cors = require('cors')
// require("dotenv").config();

// * Init
const app = express()
require('./lib/passport')

// * Public
app.use(express.static(path.join(__dirname, 'public')))

// * Settings
app.set('PORT', process.env.PORT || 8081)
app.set('views', path.join(__dirname, 'views'))
app.engine(
  '.hbs',
  exphbs({
    defaultLayout: 'main',
    layoutsDir: path.join(app.get('views'), 'layouts'),
    partialsDir: path.join(app.get('views'), 'partials'),
    extname: '.hbs',
    helpers: require('./lib/handlebars')
  })
)
app.set('view engine', '.hbs')

// * Middleware
app.use(
  session({
    secret: 'appmysql',
    resave: false,
    saveUninitialized: false,
    store: new MySqlStore(database)
  })
)
// app.use(cors())
app.use(flash())
app.use(morgan('dev'))
app.use(express.urlencoded({ extended: false })) // Aceptar datos sencillos
app.use(express.json())
app.use(passport.initialize())
app.use(passport.session())

// * Global Variables
app.use((req, res, next) => {
  app.locals.success = req.flash('success')
  app.locals.message = req.flash('message')
  app.locals.user = req.user
  // console.log(req.user)
  next()
})

// * Routes
app.use(require('./routes/authentication'))
app.use(require('./routes'))
app.use('/bot', require('./routes/bot'))
app.use(isLoggedIn) // No entrar a las rutas sin logearse
app.use(require('./routes/user'))

// * Starting Server
app.listen(app.get('PORT'), () => {
  console.log(`Server on port ${app.get('PORT')}`)
})

// * 404
app.use(error404)
