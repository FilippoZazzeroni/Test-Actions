
result=$(git status --porcelain)
echo $result
if [[ $result ]]; then
    echo "changes_detected=false"
else
    echo "changes_detected=true"
fi
