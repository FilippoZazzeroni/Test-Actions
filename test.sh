if git status --porcelain; then
    echo "changes_detected=false"
else
    echo "changes_detected=true"
fi
