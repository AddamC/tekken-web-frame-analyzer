const express = require('express');
const router = express.Router();

let characters = require("../dummyDatabase");
router.get("/list", async(req, res) => {
    try {
        res.status(200).json({
            data: characters
        });
    } catch (err) {
        res.status(400).json({
            message: "some error",
            err
        });
    }
});

module.exports = router;