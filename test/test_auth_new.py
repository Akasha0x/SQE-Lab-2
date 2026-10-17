# Target: verify_reset_token() valid token returns True 
import pytest
import auth

def test_verify_reset_token_accepts_valid_token(): 
    token = auth.generate_reset_token("student@uni.edu") 
    assert auth.verify_reset_token(token) is True 
  
  
# Target: verify_reset_token() unknown token returns False 
def test_verify_reset_token_rejects_unknown_token(): 
    assert auth.verify_reset_token("no-such-token") is False 
  
  
# Target: verify_reset_token() expired token returns False 
def test_verify_reset_token_rejects_expired_token(): 
    token = auth.generate_reset_token("student@uni.edu", hours_ago=2) 
    assert auth.verify_reset_token(token) is False 
  
  
# Target: verify_reset_token() used token returns False 
def test_verify_reset_token_rejects_used_token(): 
    token = auth.generate_reset_token("student@uni.edu") 
    auth.mark_token_used(token) 
    assert auth.verify_reset_token(token) is False

def test_check_lockout_blocks_already_locked_account(): 
    auth.lock_account("student@uni.edu") 
    assert auth.check_lockout("student@uni.edu", attempt_count=0) is False 
  
  
# Target: check_lockout() attempt_count below 3 returns True 
def test_check_lockout_allows_two_failed_attempts(): 
    assert auth.check_lockout("student@uni.edu", attempt_count=2) is True 
    assert auth.is_locked("student@uni.edu") is False 
  
  
# Target: check_lockout() unknown account with 3 attempts (user is None branch) 
def test_check_lockout_blocks_unknown_account_at_three_attempts(): 
    assert auth.check_lockout("nobody@uni.edu", attempt_count=3) is False 
# Target: validate_login() email not registered 
def test_validate_login_rejects_unregistered_email(): 
    result = auth.validate_login("ghost@uni.edu", "ValidPass1") 
    assert result["success"] is False 
    assert result["user_id"] is None 
    assert result["error"] == "Invalid credentials" 
  
  
# Target: validate_login() locked account is refused 
def test_validate_login_refuses_locked_account(): 
    auth.lock_account("student@uni.edu") 
    result = auth.validate_login("student@uni.edu", "ValidPass1") 
    assert result["success"] is False 
    assert result["error"] == "Account is locked" 
  
  
# Target: validate_login() third wrong password locks the account 
def test_validate_login_locks_account_after_three_wrong_passwords(): 
    for _ in range(3): 
        auth.validate_login("student@uni.edu", "WrongPass9") 
    assert auth.is_locked("student@uni.edu") is True