if git diff-index --quiet HEAD; then
    echo "changes_detected=false"
else
    echo "changes_detected=true"
fi
