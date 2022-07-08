<<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <title>login</title>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <link rel='stylesheet' type='text/css' media='screen' href='login2.css'>
</head>
<body>
    <form method="post" action="login.php" name="signup-form">
        <label class="title">sistemas embebidos</label>
        <div class="form-element">
            <label>Username</label>
            <input type="text" name="username" pattern="[a-zA-Z0-9]+"required />
        </div>
        <button type="submit" name="register" value="register">Register
        </button>
    </form>
</body>
</html>
