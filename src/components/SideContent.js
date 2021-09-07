import React from 'react'

const SideContent = () => {
  const Categories = [
    { name: 'Category 1', url: 'url-1' },
    { name: 'Category 2', url: 'url-2' },
    { name: 'Category 3', url: 'url-3' },
    { name: 'Category 4', url: 'url-4' },
    { name: 'Category 5', url: 'url-5' },
    { name: 'Category 6', url: 'url-6' },
    { name: 'Category 7', url: 'url-7' },
    { name: 'Category 8', url: 'url-8' },
    { name: 'Category 9', url: 'url-9' },
    { name: 'Category 10', url: 'url-10' },
  ]

  return (
    <>
      <h1 className="text-white transition dark:text-gray-300 pl-7 py-5 text-xl bg-indigo-600 dark:bg-gray-900 mb-1 rounded">Category</h1>
      <div className="bg-indigo-300 rounded transition dark:bg-gray-700 mb-5 ">
        {
          Categories.map((x) => {
            return (
              <div className="px-5 py-3 h-10 text-center">
                <div className="overflow-ellipsis overflow-hidden h-24">
                  <a href={x.url} className="text-white transition dark:text-gray-300">{x.name}</a>
                </div>
              </div>
            )
          })
        }
      </div>
    </>
  )
}

export default SideContent
