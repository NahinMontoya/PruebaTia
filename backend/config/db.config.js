module.exports = {
    HOST: "localhost",
    USER: "postgres",
    PASSWORD: "JosueDenver",
    DB: "postgres",
    dialect: "postgres",
    pool: {
      max: 100,
      min: 0,
      acquire: 30000,
      idle: 10000,
    },
    dialectOptions: {
      useUTC: true,
    } 
  };